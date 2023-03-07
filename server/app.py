from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': 'http://localhost:*/*'}})


@app.route('/calc', methods=['POST'])
def calc():
  response_object = {'status': 'success'}
  post_data = request.get_json()
  problem = post_data[ : -1]
  md = bool(True)
  i = 0
  print(problem)
  while(len(problem) > 1):
    for item in problem:
      if md:
        while(i < len(problem)):
          print(i, len(problem))
          if isinstance(item, str):
            match item:
              case 'x':
                answer = problem[problem.index(item) - 1] * problem[problem.index(item) + 1]
                print('before', problem)
                problem.insert(problem.index(item) - 1, answer)
                print('problem', problem)
                del problem[problem.index(item) - 1:problem.index(item) + 2] 
                print('after', problem)
                i += 1
                break
              case '÷':
                answer = problem[problem.index(item) - 1] / problem[problem.index(item) + 1]
                print('before', problem)
                problem.insert(problem.index(item) - 1, answer)
                print('problem', problem)
                del problem[problem.index(item) - 1:problem.index(item) + 2] 
                print('after', problem)
                i += 1
                break
              case _:
                i += 1
                break
          else:
            i += 1
            break
        else:
          md = False
          break
      else:
        print('here')
        if isinstance(item, str):
          match item:
            case '+':
              answer = problem[problem.index(item) - 1] + problem[problem.index(item) + 1]
              print('before', problem)
              problem.insert(problem.index(item) - 1, answer)
              print('problem', problem)
              del problem[problem.index(item) - 1:problem.index(item) + 2] 
              print('after', problem)
              break
            case '-':
              answer = problem[problem.index(item) - 1] - problem[problem.index(item) + 1]
              print('before', problem)
              problem.insert(problem.index(item) - 1, answer)
              print('problem', problem)
              del problem[problem.index(item) - 1:problem.index(item) + 2] 
              print('after', problem)
              break
        else:
          pass
  response_object['answer'] = problem
  return jsonify(response_object)


if __name__ == '__main__':
    app.run()
