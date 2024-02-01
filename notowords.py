def spell_out_numbers(inputs):
    spelled_numbers = []

    for num in inputs:
        try:
            spelled_number = ''
            if num < 0:
                spelled_number += 'negative '
            spelled_number += convert_to_words(abs(num))
            spelled_numbers.append(spelled_number)
        except ValueError:
            spelled_numbers.append('Invalid input')

    return spelled_numbers

def convert_to_words(num):
    units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    if 1 <= num <= 9:
        return units[num]

    elif 11 <= num <= 19:
        return teens[num - 11]

    elif 10 <= num <= 99:
        return tens[num // 10 - 1] + ('' if num % 10 == 0 else ' ' + units[num % 10])

    elif 100 <= num <= 999:
        return units[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' and ' + convert_to_words(num % 100))

    elif 1000 <= num <= 999999:
        return convert_to_words(num // 1000) + ' Thousand' + ('' if num % 1000 == 0 else ' ' + convert_to_words(num % 1000))

    elif 1000000 <= num <= 999999999:
        return convert_to_words(num // 1000000) + ' Million' + ('' if num % 1000000 == 0 else ' ' + convert_to_words(num % 1000000))

    else:
        raise ValueError('Input out of supported range')

# Example usage:
inputs = [123, -456, 789.5, 0, -1000000]
result = spell_out_numbers(inputs)
print(result)
