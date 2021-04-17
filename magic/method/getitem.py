class Persons:

    def __getitem__(self, item):
        return range(1, 10)[item]

ps = Persons()

for p in ps:
    print(p)

# print(len(ps))

print(ps[11])