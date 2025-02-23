from seven_segment_display.seven_segment import SevenSegment


def validate_binary(binary):
    if len(binary) != 8: raise ValueError("Binary must be 8 bytes long")

def is_on(binary_number: str):
    if binary_number[7] == "1": return True

def display(board: list) -> None:
    response = ""
    for row in board:
        for col in row:
            response += " " + col
        response += "\n"
    print(response)


segment = SevenSegment()
binary = input("enter: ")

try:
    validate_binary(binary)
except ValueError as e:
    print("Invalid binary.\nerror message:", e)
    exit(1)

if is_on(binary):
    match binary:
        case "01100001":
            array_board = segment.draw_one()
            display(array_board)
        case "11011011":
            array_board = segment.draw_two()
            display(array_board)
        case "11110011":
            array_board = segment.draw_three()
            display(array_board)
        case "01100111":
            array_board = segment.draw_four()
            display(array_board)
        case "10110111":
            array_board = segment.draw_five()
            display(array_board)
        case "10111111":
            array_board = segment.draw_six()
            display(array_board)
        case "11100001":
            array_board = segment.draw_seven()
            display(array_board)
        case "11111111":
            array_board = segment.draw_eight()
            display(array_board)
        case "11110111":
            array_board = segment.draw_nine()
            display(array_board)




