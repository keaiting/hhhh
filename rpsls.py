#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020..4.14
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "��":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4

    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��





def number_to_name(number):
    if number == 0:
        return "ʯͷ"
    if number == 1:
        return "ʷ����"
    if number == 2:
        return "��"
    if number == 3:
        return "����"
    if number == 4:
        return "����"
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):
    player_choice_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 4)
    comp_choice = number_to_name(comp_number)
    print("����ѡ��Ϊ��"+player_choice)
    print("�������ѡ��Ϊ��"+comp_choice)
    if (comp_number, player_choice_number) == (0, 3) or (comp_number, player_choice_number) == (0, 4) or (
    comp_number, player_choice_number) == (1, 4) or (comp_number, player_choice_number) == (1, 0) or (
    comp_number, player_choice_number) == (2, 0) or (comp_number, player_choice_number) == (2, 1):
        print("�����Ӯ��")
    elif (comp_number, player_choice_number) == (3, 1) or (comp_number, player_choice_number) == (3, 2) or (
    comp_number, player_choice_number) == (4, 3) or (comp_number, player_choice_number) == (4, 2):
        print("�����Ӯ��")
    elif (comp_number, player_choice_number) == (0, 0) or (comp_number, player_choice_number) == (1, 1) or (
    comp_number, player_choice_number) == (2, 2) or (comp_number, player_choice_number) == (3, 3) or (
    comp_number, player_choice_number) == (4, 4) or (comp_number, player_choice_number) == (5, 5):
        print("���ͼ��������һ����")
    else:
        print("��Ӯ��")
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """





    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name in ["ʯͷ","ʷ����","����","��","����"]:
    print("----------------")
    rpsls(choice_name)
else :
    print("Error: No Correct Name��")


