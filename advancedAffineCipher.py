class AffineCipher:
    def translate(key, message, mode):
        keyA, keyB = getKeyParts(key)
        checkKeys(keyA, keyB, mode)
        text = ''
        if mode == 'decrypt':
            modInverseOfKeyA = findModInverse(keyA, len(SYMBOLS))
        for symbol in message:
            if symbol in SYMBOLS:
                symIndex = SYMBOLS.find(symbol)
                if mode == 'encrypt':
                    text += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
                elif mode == 'decrypt':
                    text += SYMBOLS[(symIndex - keyB) *
                                    modInverseOfKeyA % len(SYMBOLS)]
            else:
                text += symbol
        return text

    def keyTest(message):
        for keyA in range(2, 100):
            key = keyA * len(SYMBOLS) + 1

            if gcd(keyA, len(SYMBOLS)) == 1:
                print(keyA, AffineCipher.translate(key, message, 'encrypt'))

    def file(key, mode, inputFile, outputFile):
        if not os.path.exists(inputFile):
            print('The file %s does not exist. Quitting...' % (inputFile))
            sys.exit()
        if os.path.exists(outputFile):
            print('This will overwrite the file %s.' +
                  ' (C)ontinue or (Q)uit?' % (outputFile))
            response = input('> ')
            if not response.lower().startswith('c'):
                sys.exit()
        fileObj = open(inputFile)
        content = fileObj.read()
        fileObj.close()
        print('%sing...' % (mode.title()))
        # Measure how long the encryption/decryption takes.
        startTime = time.time()
        translated = AffineCipher.translate(key, content, mode)
        totalTime = round(time.time() - startTime, 2)
        print('%sion time: %s seconds' % (mode.title(), totalTime))
        # Write out the translated message to the output file.
        outputFileObj = open(outputFile, 'w')
        outputFileObj.write(translated)
        outputFileObj.close()
        print('Done %sing %s (%s characters).' % (mode, inputFile,
                                                  len(content)))
        print('%sed file is %s.' % (mode.title(), outputFile))
