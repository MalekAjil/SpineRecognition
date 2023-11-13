class LML:
    id = 0
    name = ''
    pos = [0.0, 0.0, 0.0]

    def __int__(self):
        self.id = 0
        self.name = ''
        self.pos = [0.0, 0.0, 0.0]

    # def __int__(self, id, name, pos):
    #     self.id = id
    #     self.name = name
    #     self.pos = pos


def read_lml(filename):
    lml = []
    try:
        # [nam, path] = uigetfile('*.lml')
        # filename = fullfile(path, nam)

        fid = open(filename, 'r')
        print('Loading spine landmark file: ' + filename + '...')

        count = 0
        fid.readline()
        for line in fid.readlines():
            words = line.split('\t')
            id = int(words[0])
            name = words[1]
            pos = list(map(float, words[2:5]))

            lml.append(LML())
            lml[count].id = id
            lml[count].name = name
            lml[count].pos = pos

            count = count + 1
        print([str(len[lml]) + ' landmarks found: ' + lml[1].name + ' -> ' + lml[-1].name])
    except Exception as e:
        print(e)
    finally:
        fid.close()
        return lml
