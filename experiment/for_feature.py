contents = ['Vovatest', 'Vitatest', 'Mashatest']
filenames = ['doc.txt', 'report.txt', 'other.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    file.close()