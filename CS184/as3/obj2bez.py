""" Takes in an obj file and turns it into a bez file """
""" By Alan Yao """
import sys

def load_obj_file(filename):
    """Loads a Wavefront OBJ file. """
    """Parser credit: pygame """
    vertices = [0]
    normals = [0]
    texcoords = [0]
    faces = [0]
    max_val = 0.0

    material = None
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'v':
            v = map(float, values[1:4])
            vertices.append(v)
            max_val = max(max_val, max(v))
        elif values[0] == 'vn':
            v = map(float, values[1:4])
            normals.append(v)
        elif values[0] == 'vt':
            texcoords.append(map(float, values[1:3]))
        elif values[0] in ('usemtl', 'usemat'):
            material = values[1]
        elif values[0] == 'mtllib':
            continue
        elif values[0] == 'f':
            face = []
            texcoords = []
            norms = []
            for v in values[1:]:
                w = v.split('/')
                face.append(int(w[0]))
                if len(w) >= 2 and len(w[1]) > 0:
                    texcoords.append(int(w[1]))
                else:
                    texcoords.append(0)
                if len(w) >= 3 and len(w[2]) > 0:
                    norms.append(int(w[2]))
                else:
                    norms.append(0)
            faces.append((face, norms, texcoords, material))

    #Renormalize
    if max_val > 3.0:
      ratio = 3.0/max_val
      new_vert = [0] + [[ratio*v for v in vert] for vert in vertices[1:]]
      vertices = new_vert

    new_filename = filename[:-3] + "bez"
    out = open(new_filename, 'w+')
    for tup in faces[1:]:
        face, norms, texcoords, material = tup
        v1 = vertices[face[0]]
        v2 = vertices[face[1]]
        v3 = vertices[face[2]]
        if len(face) == 4:
            v4 = vertices[face[3]]
        else:
            v4 = v3
            #Perturbation to avoid major degeneracies
            v4[0] += 0.001
            v4[1] += 0.001
            v4[2] += 0.001
        s1 = v_to_s(v1) + v_to_s(v1) + v_to_s(v2) + v_to_s(v2) + '\n'
        s2 = v_to_s(v3) + v_to_s(v3) + v_to_s(v4) + v_to_s(v4) + '\n'
        out.write(s1)
        out.write(s1)
        out.write(s2)
        out.write(s2)
    out.close()

def v_to_s(v):
    """ v = [a, b, c] """
    return ' ' + str(v[0]) + ' ' + str(v[1]) + ' ' + str(v[2]) + ' '

def main(argv):
    if len(argv) < 2:
        print "Provide an input filename"
        sys.exit(2)
    load_obj_file(argv[1])



main(sys.argv)




