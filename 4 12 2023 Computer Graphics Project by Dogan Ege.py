# Copyright © 2023 Dogan Ege BULTE
# https://github.com/Dege34
# dege.bulte@studenti.polito.it
def take_indicates(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as input_file:
            # here, i am reading the lines in the input file
            lines = input_file.readlines()

            # in line 33, initialize the indices list
            indices_strips = []

            # in line 36, iterate through each line
            for i in range(len(lines)):

                line = lines[i].strip()

                # i am spliting the line into indicess
                indices = line.split()

                #  i am checking to the: if it's not the first line

                if i > 0:
                    # Get the last two vertices from the previous strip
                    last_vertex1 = indices_strips[-2]
                    last_vertex2 = indices_strips[-1]

                    # i found the common vertices between the current strip and previous strip
                    common_vertices = [v for v in indices if v == last_vertex1 or v == last_vertex2]


                    # i append the remaining vertices to the index strips list
                    indices_strips.extend([v for v in indices if v not in common_vertices])

                else:
                    # appending all vertices to the index strips list for the first line
                    indices_strips.extend(indices)

        return indices_strips


    except OSError as issue:
        print("HOMMER ! WE HAVE PROBLEM ABOUT FILE !!")
        exit(1)



def write_indices(filename,strips):
    try:
        with open(filename, 'w') as output_file:
        # i write the indices strips as one line in the output file
            output_file.write(' '.join(strips))

    except OSError as problem:
        print("HOMMER ! WE HAVE PROBLEM ABOUT FILE !!")
        exit(2)
    
# open the main function for collecting all of them
def main():
    question_about_input = input("Write a indices file name with .txt:\n")

    question_about_output = input("Write a indices strips name with .txt\n")

    designation_file = take_indicates(question_about_input)
    write_indices(question_about_output,designation_file)

    print("\nThe result was uploaded to the folder named '{}' that you wrote.".format(question_about_output))


if __name__ == "__main__":
    main()
