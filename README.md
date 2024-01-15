# Course Level Programming Assignment - Programming a Calculator using Python


## Objectives

  - Extend the functionali of the the calculator to save and display the past results of the arithmetic operations

## Stage 2: Save and display calculation history of the calculator

  - In this second stage of the assignment you will extend the given calculator program to record the calculations, and recall them as a list using an additional command '?'.

## Task 1: Study the given code in the answer box and extend it to save each executed operation in a Python List

- Declare a list to store the previous operations
- Save the operator, operands and the results as a single string, for each operation after each calculation
  
## Task 2: implement a history() function to handle the operation '?'

- Display the complete saved list of operations (in the order of execution) using a new command ‘?’
- If there are no previous calculations when the history '?' command is used, you can display the following message
  
     "No past calculations to show"

  
  <table>
    <thead>
        <tr>
            <th>Input</th>
            <th>Result</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>#</td>
            <td>
                <p>Select operation.</p>
                <p>1.Add : +</p>
                <p>2.Subtract : -</p>
                <p>3.Multiply : *</p>
                <p>4.Divide : /</p>
                <p>5.Power : ^</p>
                <p>6.Remainder: %</p>
                <p>7.Terminate: #</p>
                <p>8.Reset : $</p>
                <p>8.History : ?</p>
                <p>Enter choice(+,-,*,/,^,%,#,$): #</p>
                <p>Done. Terminating</p>
            </td>
        </tr>
                <tr>
            <td>
                <p>+</p>
                <p>4</p>
                <p>3</p>
                <p>+</p>
                <p>6</p>
                <p>2</p>
                <p>-</p>
                <p>5</p>
                <p>2</p>
                <p>?</p>
                <p>#</p>
            </td>
            <td>
                <p>Select operation.</p>
                <p>1.Add : +</p>
                <p>2.Subtract : -</p>
                <p>3.Multiply : *</p>
                <p>4.Divide : /</p>
                <p>5.Power : ^</p>
                <p>6.Remainder: %</p>
                <p>7.Terminate: #</p>
                <p>8.Reset : $</p>
                <p>8.History : ?</p>
                <p>Enter choice(+,-,*,/,^,%,#,$): +</p>
                <p>Enter first number: 4</p>
                <p>Enter second number: 3</p>
                <p>4.0 + 3.0 = 7.0</p>
                <p>Select operation.</p>
                <p>1.Add : +</p>
                <p>2.Subtract : -</p>
                <p>3.Multiply : *</p>
                <p>4.Divide : /</p>
                <p>5.Power : ^</p>
                <p>6.Remainder: %</p>
                <p>7.Terminate: #</p>
                <p>8.Reset : $</p>
                <p>8.History : ?</p>
                <p>Enter choice(+,-,*,/,^,%,#,$): +</p>
                <p>Enter first number: 6</p>
                <p>Enter second number: 2</p>
                <p>6.0 + 2.0 = 8.0</p>
                <p>Select operation.</p>
                <p>1.Add : +</p>
                <p>2.Subtract : -</p>
                <p>3.Multiply : *</p>
                <p>4.Divide : /</p>
                <p>5.Power : ^</p>
                <p>6.Remainder: %</p>
                <p>7.Terminate: #</p>
                <p>8.Reset : $</p>
                <p>8.History : ?</p>
                <p>Enter choice(+,-,*,/,^,%,#,$): -</p>
                <p>Enter first number: 5</p>
                <p>Enter second number: 2</p>
                <p>5.0 - 2.0 = 3.0</p>
                <p>Select operation.</p>
                <p>1.Add : +</p>
                <p>2.Subtract : -</p>
                <p>3.Multiply : *</p>
                <p>4.Divide : /</p>
                <p>5.Power : ^</p>
                <p>6.Remainder: %</p>
                <p>7.Terminate: #</p>
                <p>8.Reset : $</p>
                <p>8.History : ?</p>
                <p>Enter choice(+,-,*,/,^,%,#,$): ?</p>
                <p>4.0 + 3.0 = 7.0</p>
                <p>6.0 + 2.0 = 8.0</p>
                <p>5.0 - 2.0 = 3.0</p>
                <p>Select operation.</p>
                <p>1.Add : +</p>
                <p>2.Subtract : -</p>
                <p>3.Multiply : *</p>
                <p>4.Divide : /</p>
                <p>5.Power : ^</p>
                <p>6.Remainder: %</p>
                <p>7.Terminate: #</p>
                <p>8.Reset : $</p>
                <p>8.History : ?</p>
                <p>Enter choice(+,-,*,/,^,%,#,$): #</p>
                <p>Done. Terminating</p>
            </td>
        </tr>
        <tr>
    <td>
        <p>+</p>
        <p>4</p>
        <p>3</p>
        <p>/</p>
        <p>6.35</p>
        <p>2.36</p>
        <p>-</p>
        <p>5.532</p>
        <p>2.342</p>
        <p>?</p>
        <p>#</p>
    </td>
    <td>
        <p>Select operation.</p>
        <p>1.Add : +</p>
        <p>2.Subtract : -</p>
        <p>3.Multiply : *</p>
        <p>4.Divide : /</p>
        <p>5.Power : ^</p>
        <p>6.Remainder: %</p>
        <p>7.Terminate: #</p>
        <p>8.Reset : $</p>
        <p>8.History : ?</p>
        <p>Enter choice(+,-,*,/,^,%,#,$): +</p>
        <p>Enter first number: 4</p>
        <p>Enter second number: 3</p>
        <p>4.0 + 3.0 = 7.0</p>
        <p>Select operation.</p>
        <p>1.Add : +</p>
        <p>2.Subtract : -</p>
        <p>3.Multiply : *</p>
        <p>4.Divide : /</p>
        <p>5.Power : ^</p>
        <p>6.Remainder: %</p>
        <p>7.Terminate: #</p>
        <p>8.Reset : $</p>
        <p>8.History : ?</p>
        <p>Enter choice(+,-,*,/,^,%,#,$): /</p>
        <p>Enter first number: 6.35</p>
        <p>Enter second number: 2.36</p>
        <p>6.35 / 2.36 = 2.690677966101695</p>
        <p>Select operation.</p>
        <p>1.Add : +</p>
        <p>2.Subtract : -</p>
        <p>3.Multiply : *</p>
        <p>4.Divide : /</p>
        <p>5.Power : ^</p>
        <p>6.Remainder: %</p>
        <p>7.Terminate: #</p>
        <p>8.Reset : $</p>
        <p>8.History : ?</p>
        <p>Enter choice(+,-,*,/,^,%,#,$): -</p>
        <p>Enter first number: 5.532</p>
        <p>Enter second number: 2.342</p>
        <p>5.532 - 2.342 = 3.19</p>
        <p>Select operation.</p>
        <p>1.Add : +</p>
        <p>2.Subtract : -</p>
        <p>3.Multiply : *</p>
        <p>4.Divide : /</p>
        <p>5.Power : ^</p>
        <p>6.Remainder: %</p>
        <p>7.Terminate: #</p>
        <p>8.Reset : $</p>
        <p>8.History : ?</p>
        <p>Enter choice(+,-,*,/,^,%,#,$): ?</p>
        <p>4.0 + 3.0 = 7.0</p>
        <p>6.35 / 2.36 = 2.690677966101695</p>
        <p>5.532 - 2.342 = 3.19</p>
        <p>Select operation.</p>
        <p>1.Add : +</p>
        <p>2.Subtract : -</p>
        <p>3.Multiply : *</p>
        <p>4.Divide : /</p>
        <p>5.Power : ^</p>
        <p>6.Remainder: %</p>
        <p>7.Terminate: #</p>
        <p>8.Reset : $</p>
        <p>8.History : ?</p>
        <p>Enter choice(+,-,*,/,^,%,#,$): #</p>
        <p>Done. Terminating</p>
    </td>
</tr>
<tr>
    <td>
        <p>?</p>
        <p>#</p>
    </td>
    <td>
        <p>Select operation.</p>
        <p>1.Add : +</p>
        <p>2.Subtract : -</p>
        <p>3.Multiply : *</p>
        <p>4.Divide : /</p>
        <p>5.Power : ^</p>
        <p>6.Remainder: %</p>
        <p>7.Terminate: #</p>
        <p>8.Reset : $</p>
        <p>8.History : ?</p>
        <p>Enter choice(+,-,*,/,^,%,#,$): ?</p>
        <p>No past calculations to show</p>
        <p>Select operation.</p>
        <p>1.Add : +</p>
        <p>2.Subtract : -</p>
        <p>3.Multiply : *</p>
        <p>4.Divide : /</p>
        <p>5.Power : ^</p>
        <p>6.Remainder: %</p>
        <p>7.Terminate: #</p>
        <p>8.Reset : $</p>
        <p>8.History : ?</p>
        <p>Enter choice(+,-,*,/,^,%,#,$): #</p>
        <p>Done. Terminating</p>
    </td>
</tr>


    </tbody>
</table>

</body>
</html>
