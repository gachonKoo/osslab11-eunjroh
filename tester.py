- name: Run Test
  id: test
  uses: classroom-resources/autograding-io-grader@v1
  with:
    test-name: test
    setup-command: ""
    command: python tester.py
    input: ""
    expected-output: |-
      c = 5.0
      area = 314.1592653589793
    comparison-method: contains
    timeout: 10

