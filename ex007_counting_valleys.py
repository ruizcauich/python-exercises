# COUNTING VALLEYS

# Count the number of valleys based on the input
# where step = number of steps in the hike and
# path = the step type U(up) D(down)

# Taken from:
# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# UUDDDU

def counting_valleys(steps, path):
    current_height = 0
    previus_height = 0
    total_valleys = 0

    for step_type in path:
        if step_type == 'U':
            current_height += 1
        else:
            current_height -= 1

        if current_height < 0 and previus_height == 0:
            total_valleys += 1

        previus_height = current_height

    return total_valleys


if __name__ == "__main__":
    assert counting_valleys(5, "UUDDDUU") == 1, "Should be 1"
    assert counting_valleys(5, "UDDDUDUU") == 1, "Should be 1"
    assert counting_valleys(5, "DDUUDDUDUUUD") == 2, "Should be 2"
    assert counting_valleys(5, "UDUUUDUDDD") == 0, "Should be 0"
