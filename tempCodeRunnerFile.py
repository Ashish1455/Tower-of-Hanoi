if __name__ == '__main__':
    num_discs = int(input('Number of Disks: '))
    num_towers = int(input('Number of Towers: '))
    
    solver = HanoiSolver(num_discs, num_towers)
    solver.hanoi(0, num_towers - 1, num_discs, num_towers)

    print("Final Tower State:", solver.get_towers())
