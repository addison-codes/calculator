from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS to only accept requests originating from localhost for security
CORS(app, resources={r'/*': {'origins': 'http://localhost:*/*'}})

# Take in POST requests at the /calc endpoint and run calc function
@app.route('/calc', methods=['POST'])
def calc():
  response_object = {'status': 'success'}
  post_data = request.get_json()
  # Remove the trailing equals sign
  problem = post_data[ : -1]
  # Setup a boolean that will help determine when we have looped through all of the multiplication and division operators
  md = bool(True)
  # Setup iterator
  i = 0
  # Continue looping while the length of the problem of the problem array is greater than one
  while(len(problem) > 1):
    for item in problem:
      # If md is true, we'll do this first to fine all of the multiplication and division operators first to follow order of operations
      if md:
        while(i < len(problem)):
          # Check if something is a string, as we only want to operate on those
          if isinstance(item, str):
            match item:
              # If it's a 'x' we multiply the 2 items on either side of the operator, then add that answer to the problem array and remove the 3 calculated items (2 numbers and operator). I have left in the print lines to show how it adds and removes items to the problems array. Finally, no matter what always increase the iterator
              case 'x':
                answer = problem[problem.index(item) - 1] * problem[problem.index(item) + 1]
                print('before', problem)
                problem.insert(problem.index(item) - 1, answer)
                print('problem', problem)
                del problem[problem.index(item) - 1:problem.index(item) + 2] 
                print('after', problem)
                i += 1
                break
              # If it's a '÷' we divide the 2 items on either side of the operator and do the same steps as above
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
        # Once we have iterated through the whole problem array, that means that there are no more multiplication or division operators and we can move on to addition and subtraction
        else:
          md = False
          break
      else:
        if isinstance(item, str):
          match item:
            # If it's a '+' we add the 2 items on either side of the operator, then add that answer to the problem array and remove the 3 calculated items (2 numbers and operator). I have left in the print lines to show how it adds and removes items to the problems array.
            case '+':
              answer = problem[problem.index(item) - 1] + problem[problem.index(item) + 1]
              print('before', problem)
              problem.insert(problem.index(item) - 1, answer)
              print('problem', problem)
              del problem[problem.index(item) - 1:problem.index(item) + 2] 
              print('after', problem)
              break
            # If it's a '-' we subtract the 2 items on either side of the operator and do the same steps above
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
  # finally we return the problem now that it is has been iterated and all math operations completed.
  return jsonify(response_object)


if __name__ == '__main__':
    app.run()
