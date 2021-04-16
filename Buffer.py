class Buffer:
    def load_buffer(self):
        arw = open('getrude.txt', 'r')
        text = arw.readline()

        buffer = []
        count = 1

        while text != "":
            buffer.append(text)
            text = arw.readline()
            count += 1

            if count == 10 or text == "":
                #RETURN A FULL BUFFER
                buf = ''.join(buffer)
                count = 1
                yield buf

                #reset the buffer
                buffer = []

        arw.close()
