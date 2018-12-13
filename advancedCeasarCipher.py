class CeasarCipher:
    def translate(enc, key, mode):
        chars = []
        for ch in enc:
            if mode == 'encrypt':
                chars.append(chr(ord(ch) + key))
            elif mode == 'decrypt':
                chars.append(chr(ord(ch) - key))
        return ''.join(chars)

    def keyTest(message, start, stop):
        for key in range(start, stop + 1):
            print(key, CeasarCipher.translate(message, key, 'encrypt'))

    def file(key, mode, inputFile, outputFile):
        if not os.path.exists(inputFile):
            print('The file %s does not exist. Quitting...' % (inputFile))
            sys.exit()
        if os.path.exists(outputFile):
            print('This will overwrite the file %s.' +
                  '(C)ontinue or (Q)uit?' % (outputFile))
            response = input('> ')
            if not response.lower().startswith('c'):
                sys.exit()
        fileObj = open(inputFile)
        content = fileObj.read()
        fileObj.close()
        print('%sing...' % (mode.title()))
        # Measure how long the encryption/decryption takes.
        startTime = time.time()
        translated = CeasarCipher.translate(content, key, mode)
        totalTime = round(time.time() - startTime, 2)
        print('%sion time: %s seconds' % (mode.title(), totalTime))
        outputFileObj = open(outputFile, 'w')
        outputFileObj.write(translated)
        outputFileObj.close()
        print('Done %sing %s (%s characters).' %
              (mode, inputFile, len(content)))
        print('%sed file is %s.' % (mode.title(), outputFile))

    def advancedBruteForce(message, start, stop):
        for key in range(start, stop + 1):
            print(key, CeasarCipher.translate(message, key, 'decrypt'))
            
    def bruteForce(message):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
            print('Key #%s: %s' % (key, translated))
