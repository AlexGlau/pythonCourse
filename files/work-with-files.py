with open('referat.txt', 'r', encoding='utf8') as file:
    content = file.read()
    content_length = len(content)
    print(content_length)

    words = content.split(' ')
    words_amount = len(words)
    print(words_amount)

    dots_replaced = content.replace('.', '!')
    print(dots_replaced)

    with open('referat2.txt', 'w', encoding='utf8') as file2:
        file2.write(dots_replaced)
