def two_string(a, b):
  for i in range(min(len(a),len(b))):
    if a[i] == b[i]:
      print(f"Match of character '{a[i]}' found at index {i}")

two_string('python', 'py')
