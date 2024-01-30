import random
import matplotlib.pyplot as plt
import numpy as np

weights = [200, 200, 200, 199, 198, 198, 197, 197, 194, 194, 193, 192, 191, 191, 191, 190, 190, 189, 188, 188, 187, 187, 186, 185, 185, 185, 185, 184, 184, 184, 183, 183, 183, 182, 182, 182, 181, 181, 180, 179, 179, 179, 179, 178, 177, 177, 177, 177, 175, 174, 173, 173, 172, 171, 171, 171, 170, 170, 169, 169, 169, 167, 167, 165, 165, 164, 163, 163, 163, 163, 162, 161, 160, 160, 159, 158, 158, 158, 157, 156, 156, 156, 156, 156, 156, 155, 155, 155, 154, 154, 153, 152, 152, 152, 151, 151, 150, 150, 150, 150]
children_list = []
bin_num = 18
bin_size = 1000


def max_and_average_scores(gen_dict):
    if not gen_dict:
        return None

    max_fitness_child = max(gen_dict, key=lambda x: x['fitness'])['fitness']
    avg_fitness = sum(child['fitness'] for child in gen_dict) / len(gen_dict)

    print('max_fitness_child', max_fitness_child, 'avg_fitness', avg_fitness)


def generate_random_values(length):
    return [random.randint(1, bin_num) for _ in range(length)]


def mutate_list(to_be_mutated_list):
    for i in range(0, len(to_be_mutated_list)):
        random_alel = generate_random_values(1)
        to_be_mutated_list[i] = random_alel[0]
    return to_be_mutated_list


def divide_list_into_sections(my_list, num_sections):
    section_size = len(my_list) // num_sections
    divided_sections = [my_list[n * section_size: (n + 1) * section_size] for n in range(num_sections)]
    return divided_sections


def mutation(parent_list, top_num_parents, child_return_num):
    # Sort parents based on fitness in descending order
    sorted_parents = sorted(parent_list, key=lambda x: x['fitness'], reverse=True)
    top_parents = []
    total_sub_list = []
    # gene_divider_num = len(parent_list[0]['genes']) / (child_return_num / top_num_parents)
    gene_divider_num = 100
    # loop through parent number sorting them
    for parent in range(0, top_num_parents):
        # sorted_parents[parent]['fitness']
        top_parents.append(sorted_parents[parent])

    # getting total sub list of top parents from ordered list of top parents
    for parent_list in top_parents:
        sub_list = divide_list_into_sections(parent_list['genes'], int(gene_divider_num))
        # print('sub list', sub_list)
        total_sub_list.append(sub_list)

    print('total_sub_list', total_sub_list)
    combined_lists = list(zip(*total_sub_list))

    # print("ba", combined_lists)
    # print('top parents', top_parents)
    # print(gene_divider_num)
    new_gen = []
    for instance in range(0, int(child_return_num/top_num_parents)):
        after_list = []
        # Print the grouped lists
        for group in combined_lists:
            fixed_list = list(group)
            # print("Grouped elements before:", fixed_list)
            random.shuffle(fixed_list)
            # print("Grouped elements after:", fixed_list)
            after_list.append(fixed_list)
        # print(after_list)

        final_list = []
        for k in after_list:
            for l in range(0, 2):
                final_list.append(k[l])

        # print(len(final_list))

        # Separate 0s and 1s dynamically
        separated_lists = [[] for _ in range(top_num_parents)]
        for i, element in enumerate(final_list):
            separated_lists[i % top_num_parents].append(element)

        # Print the separated lists
        for i, separated_list in enumerate(separated_lists):
            # print(f"{i}s list:", separated_list)
            flattened_list = [item for sublist in separated_list for item in sublist]
            # print("Flattened list:", flattened_list)
            new_gen.append(flattened_list)

    # new_gen = sorted(new_gen, key=lambda x: sum(x), reverse=False)
    # print("new gen", len(new_gen))
    for gen in range(0, int(len(new_gen)/2)):
        new_gen[gen] = mutate_list(new_gen[gen])

    new_gen_children_list = []
    for new_gen_child in new_gen:
        fitness_rank_child = fitness_fun(new_gen_child)
        child_dict = {'genes': new_gen_child, 'fitness': fitness_rank_child}
        new_gen_children_list.append(child_dict)
    sorted_children = sorted(new_gen_children_list, key=lambda x: x['fitness'], reverse=False)
    for unfit_child in range(0, top_num_parents):
        sorted_children[unfit_child] = sorted_parents[unfit_child]
    return sorted_children


def random_binary_list(length):
    return [random.choice([0, 1]) for _ in range(length)]


def fitness_fun(child_list):
    lenchildlist = len(child_list)
    lenweightslist = len(weights)
    count = {}
    for num in range(0, len(child_list)):
        count[child_list[num]] = count.get(child_list[num], 0) + weights[num]
    fitness_num = 0
    # Check if all values occurred exactly 3 times
    for num in range(1, 11):
        if count.get(num, 0) < bin_size:
            fitness_num = fitness_num+1
    return fitness_num


def max_score(gen_dict):
    max_fitness_child = max(gen_dict, key=lambda x: x['fitness'])['fitness']
    return max_fitness_child


for i in range(10):
    length_of_list = 100
    random_list = generate_random_values(length_of_list)
    fitness_rank = fitness_fun(random_list)
    child_dict = {'genes': random_list, 'fitness': fitness_rank}
    children_list.append(child_dict)

print(len(children_list))
print("children list", children_list)
max_and_average_scores(children_list)
children_per_gen = 30

gen1 = mutation(children_list, 2, children_per_gen)
max_and_average_scores(gen1)
gen2 = mutation(gen1, 2, children_per_gen)
max_and_average_scores(gen2)
gen3 = mutation(gen2, 2, children_per_gen)
max_and_average_scores(gen3)
gen4 = mutation(gen3, 2, children_per_gen)
max_and_average_scores(gen4)
gen5 = mutation(gen4, 2, children_per_gen)
max_and_average_scores(gen5)
gen6 = mutation(gen5, 2, children_per_gen)
max_and_average_scores(gen6)
gen7 = mutation(gen6, 2, children_per_gen)
max_and_average_scores(gen7)
gen8 = mutation(gen7, 2, children_per_gen)
max_and_average_scores(gen8)
gen9 = mutation(gen8, 2, children_per_gen)
max_and_average_scores(gen9)
gen10 = mutation(gen9, 2, children_per_gen)
max_and_average_scores(gen10)
gen11 = mutation(gen10, 2, children_per_gen)
max_and_average_scores(gen11)
gen12 = mutation(gen11, 2, children_per_gen)
max_and_average_scores(gen12)
gen13 = mutation(gen12, 2, children_per_gen)
max_and_average_scores(gen13)
gen14 = mutation(gen13, 2, children_per_gen)
max_and_average_scores(gen14)
gen15 = mutation(gen14, 2, children_per_gen)
max_and_average_scores(gen15)
gen16 = mutation(gen15, 2, children_per_gen)
max_and_average_scores(gen16)
gen17 = mutation(gen16, 2, children_per_gen)
max_and_average_scores(gen17)
gen18 = mutation(gen17, 2, children_per_gen)
max_and_average_scores(gen18)
gen19 = mutation(gen18, 2, children_per_gen)
max_and_average_scores(gen19)
gen20 = mutation(gen19, 2, children_per_gen)
max_and_average_scores(gen20)
gen21 = mutation(gen20, 2, children_per_gen)
max_and_average_scores(gen21)
gen22 = mutation(gen21, 2, children_per_gen)
max_and_average_scores(gen22)
gen23 = mutation(gen22, 2, children_per_gen)
max_and_average_scores(gen23)
gen24 = mutation(gen23, 2, children_per_gen)
max_and_average_scores(gen24)
gen25 = mutation(gen24, 2, children_per_gen)
max_and_average_scores(gen25)
gen26 = mutation(gen25, 2, children_per_gen)
max_and_average_scores(gen26)
gen27 = mutation(gen26, 2, children_per_gen)
max_and_average_scores(gen27)
gen28 = mutation(gen27, 2, children_per_gen)
max_and_average_scores(gen28)
gen29 = mutation(gen28, 2, children_per_gen)
max_and_average_scores(gen29)
gen30 = mutation(gen29, 2, children_per_gen)
max_and_average_scores(gen30)

ypoints = np.array([max_score(children_list), max_score(gen1), max_score(gen2), max_score(gen3), max_score(gen4), max_score(gen5), max_score(gen6), max_score(gen7), max_score(gen8), max_score(gen9), max_score(gen10), max_score(gen11), max_score(gen12), max_score(gen13), max_score(gen14), max_score(gen15), max_score(gen16), max_score(gen17), max_score(gen18), max_score(gen19), max_score(gen20), max_score(gen21), max_score(gen22), max_score(gen23), max_score(gen24), max_score(gen25), max_score(gen26), max_score(gen27), max_score(gen28), max_score(gen29), max_score(gen30)])

plt.plot(ypoints, marker='o')
plt.show()
