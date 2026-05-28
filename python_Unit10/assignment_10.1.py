import random


def fusion(lst1):

    cluster = {}

    sorted_list = sorted(lst1)
    copy_list = sorted_list[:]

    for i in range(0, len(sorted_list)-1):
        if sorted_list[i+1] == sorted_list[i]+1:
            copy_list[i+1] = copy_list[i]
    
    for i in copy_list:
        if i not in cluster:
            cluster[i] = 1
        else:
            cluster[i] += 1

    return cluster

def create_particles(max_coordinates):
    
    particles = set()
    n = max_coordinates ** 3

    for _ in range(n):
        x = random.randint(0, max_coordinates)
        y = random.randint(0, max_coordinates)
        z = random.randint(0, max_coordinates)
        coordinate = (x, y, z)
        particles.add(coordinate)

    return particles

def build_dict_xy(particles):

    xy_set = set()
    xy_dict = {}
  

    for particle in particles:

        x = particle[0]
        y = particle[1]
        xy = (x,y)
        xy_set.add(xy)

        if xy in xy_set:
            if xy not in xy_dict:
                z = particle[2]
                z_list = [z]
                xy_dict[xy] = z_list
            else:
                xy_dict[xy].append(z)

    return xy_dict

def main():
    # list1 = [11, 4, 16, 3, 2, 5, 15, 8]
    # cluster = fusion(list1)
    # print(cluster)

    particle = create_particles(2)
    print(particle)
    print(build_dict_xy(particle))


if __name__ == "__main__":
    main()
