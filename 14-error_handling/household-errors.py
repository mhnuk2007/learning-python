""" household-errors.py - Handling Household Problems with Custom Exceptions """

class ElectricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f'The {self.device} is {self.problem}!'


class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return f'The {self.device} is {self.problem}!'


def cause_error(error_type):
    if error_type == 'electrical':
        raise ElectricalError('circuit breaker', 'overloaded')
    elif error_type == 'plumbing':
        raise PlumbingError('dishwasher', 'spraying water')
    else:
        raise Exception('Generic household problem')


if __name__ == "__main__":
    # Try different errors
    for problem in ['electrical', 'plumbing', 'yard']:
        try:
            cause_error(problem)
        except ElectricalError as e:
            print(e)
            print('Fix it electrically.')
        except PlumbingError as e:
            print(e)
            print('Call the plumber.')
        except Exception as e:
            print(e)
            print('Call the landlord.')