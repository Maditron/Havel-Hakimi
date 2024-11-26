def havel_hakimi(sequence):
    while sequence:
        sequence.sort(reverse=True)
        largest = sequence.pop(0)
        if largest > len(sequence):
            return False


        for i in range(largest):
            sequence[i] -= 1
            if sequence[i] < 0:
                return False  

    return True 

# مثال
degree_sequence = [4, 3, 3, 2, 2, 1]
print("Is the sequence graphical?", havel_hakimi(degree_sequence))

degree_sequence = [3, 3, 2, 2, 2]
print("Is the sequence graphical?", havel_hakimi(degree_sequence)) 