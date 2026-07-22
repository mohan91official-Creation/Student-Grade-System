# Test Results

The program was tested with Python 3.12. The outputs below cover all grade bands, exact boundaries, a decimal mark, and invalid inputs.

## Required sample runs

```text
Enter your mark (0-100): 95
Mark: 95 -> Grade: A

Enter your mark (0-100): 85
Mark: 85 -> Grade: B

Enter your mark (0-100): 75
Mark: 75 -> Grade: C

Enter your mark (0-100): 65
Mark: 65 -> Grade: D

Enter your mark (0-100): 55
Mark: 55 -> Grade: E
```

## Boundary tests

| Input | Expected result |
|---:|:---|
| 100 | A |
| 90 | A |
| 89 | B |
| 80 | B |
| 79 | C |
| 70 | C |
| 69 | D |
| 60 | D |
| 59 | E |
| 0 | E |
| 85.5 | B |

## Invalid input tests

These entries all produce `Invalid input: please enter a number from 0 to 100.` and the program exits normally:

- `101`
- `-1`
- `hello`
- `nan`

## Invalid-input explanation for submission

I used exception handling to catch entries that cannot be converted to a number. I also check that the mark is a finite number within the allowed 0-100 range, so invalid entries receive a clear message and the program does not crash.
