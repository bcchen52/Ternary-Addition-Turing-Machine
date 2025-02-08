def validate_results(expectedfile, resultfile):
    expected_output = open(expectedfile).readline()
    result = open(resultfile).read().split()
    result_output = result[1]
    if(expected_output == result_output):
        print("Result matches expected.")
    else:
        print(len(result_output))
        print(len(expected_output))
        print(f"Expected: {expected_output}, does not match Result: {result_output}.")

validate_results("expected_cases.txt", "result.txt")