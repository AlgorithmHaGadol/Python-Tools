class TranspositionCipher:
    def encrypt(key, message):
        ciphertext = [''] * key
        for col in range(key):
            pointer = col
            while pointer < len(message):
                ciphertext[col] += message[pointer]
                pointer += key
        return ''.join(ciphertext)

    def decrypt(key, message):
        numOfColumns = math.ceil(len(message) / key)
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
        plaintext = [''] * numOfColumns
        col = 0
        row = 0
        for symbol in message:
            plaintext[col] += symbol
            col += 1
            if (col == numOfColumns) or (col == numOfColumns - 1 and
                                         row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
        return ''.join(plaintext)

    def file(key, mode, inputFile, outputFile):
        if not os.path.exists(inputFile):
            print('The file %s does not exist. Quitting...' % (inputFile))
            sys.exit()
        if os.path.exists(outputFile):
            print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %
                  (outputFile))
            response = input('> ')
            if not response.lower().startswith('c'):
                sys.exit()
        fileObj = open(inputFile)
        content = fileObj.read()
        fileObj.close()
        print('%sing...' % (mode.title()))
        # Measure how long the encryption/decryption takes.
        startTime = time.time()
        if mode == 'encrypt':
            translated = TranspositionCipher.encrypt(key, content)
        elif mode == 'decrypt':
            translated = TranspositionCipher.decrypt(key, content)
        totalTime = round(time.time() - startTime, 2)
        print('%sion time: %s seconds' % (mode.title(), totalTime))
        # Write out the translated message to the output file.
        outputFileObj = open(outputFile, 'w')
        outputFileObj.write(translated)
        outputFileObj.close()

        print('Done %sing %s (%s characters).' % (mode,
                                                  inputFile, len(content)))
        print('%sed file is %s.' % (mode.title(), outputFile))
