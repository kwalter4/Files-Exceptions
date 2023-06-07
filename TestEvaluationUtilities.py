def getOutputFromInput(module, input_values):
    output = []

    def mock_print(*standard_outputs):
        standard_output = " ".join(map(str, standard_outputs))
        output.append(standard_output)

    def mock_input(standard_output):
        output.append(standard_output)
        return input_values.pop(0)

    module.input = mock_input
    module.print = mock_print
    module.main()

    return output