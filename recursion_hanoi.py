'''Hanoi towers.

'''

def replace_hanoi_towers(disk_amount: int, target_pos: int):
    '''Create list of towers and start recursion replacement.
	disk_amount -- count of disks (int)
	target_pos -- target position of the tower (int)

    '''
    pyramid = list(range(disk_amount, 0, -1))
    towers = [pyramid, [0], [0]]
    recursion_hanoi(towers, disk_amount, 0, target_pos)
    return towers

def recursion_hanoi(towers: list, disk_amount: int, tower_pos: int, target_pos: int):
    '''Replace pyramid to selected position with recursion.
	towers -- list of disk's positions (list).
	disk_amount -- amount of disk in processed tower (int)
    tower_pos -- position of processed tower (int)
    target_pos -- position where processed tower must be after
				  completing of this recurrent case (int).

    '''
    tmp_pos = 3 - target_pos - tower_pos

    if disk_amount >= 1:
        recursion_hanoi(towers, disk_amount - 1, tower_pos, tmp_pos)
        replace_disk(towers, tower_pos, target_pos)
        recursion_hanoi(towers, disk_amount - 1, tmp_pos, target_pos)

def replace_disk(towers, from_pos, to_pos):
    '''Replace top element from from_pos-tower to to_pos-tower.
    towers -- current list of towers (list)
    from_pos -- position of moved disk (int)
    to_pos -- target position of disk's moving (int)

    '''
    print(from_pos, to_pos, towers, sep = '; ')
    from_tower = towers[from_pos]
    to_tower = towers[to_pos]
    disk = from_tower.pop()
    if len(from_tower) == 0:
        from_tower.append(0)
    if len(to_tower) == 1 and to_tower[0] == 0:
        to_tower[0] = disk
    else:
        to_tower.append(disk)

def test_hanoi():
    '''Common tests for module.

    '''
    pyramid3 = list(range(3, 0, -1))
    pyramid5 = list(range(5, 0, -1))
    pyramid8 = list(range(8, 0, -1))

    target_pos = 2
    disk_amount = 3
    res = [[0], [0], pyramid3]
    test_case_hanoi(disk_amount, target_pos, res, "1")

    target_pos = 1
    disk_amount = 5
    res = [[0], pyramid5, [0]]
    test_case_hanoi(disk_amount, target_pos, res, "2")

    target_pos = 2
    disk_amount = 8
    res = [[0], [0], pyramid8]
    test_case_hanoi(disk_amount, target_pos, res, "3")

def test_case_hanoi(disk_amount, target_pos, res, case_name):
    '''Test case for Hanoi.

    '''
    print("testcase #", case_name, ": ", end="")
    res_counted = replace_hanoi_towers(disk_amount, target_pos)
    print("Ok" if res == res_counted else "Fail", res_counted, sep = '; ')
    print(res, res_counted, sep = "; ")

if __name__ == '__main__':
    test_hanoi()
