music = input()

c_major_centers = {'C', 'F', 'G'}
a_minor_centers = {'A', 'D', 'E'}

first_notes = []
for measure in music.split('|'):
    if measure:
        first_notes.append(measure[0])

c_major_count = sum(note in c_major_centers for note in first_notes)
a_minor_count = sum(note in a_minor_centers for note in first_notes)

if c_major_count > a_minor_count:
    print("C-major")
elif c_major_count < a_minor_count:
    print("A-minor")
else:
    last_note = music[-1]
    if last_note in a_minor_centers:
        print("A-minor")
    else:
        print("C-major")