import argparse
def create_parser():

    # Création du parseur de ligne de commande
    parser = argparse.ArgumentParser(prog='Task_manager', usage='%(prog)s [options]',description='A simple task manager')

    # Ajout d’un argumentpositionnel (le fichier contenant les tâches)
    parser.add_argument('file', help='The tasks file')

    # Ajout d’un sous-parseur pour les sous-commandes
    subparsers = parser.add_subparsers(usage='%(prog)s [options]',help='The commands to manage orders',
    dest='command', required=True)

    # Création du parseur pour la commandeadd
    parser_add = subparsers.add_parser('add', usage='%(prog)s add [options]', help='Add a new task. The rest of the command line is used for the task details, the default being "no details".')
    parser_add.add_argument('details', nargs='*', default=["no details"],
    help="task details")
    parser_add.add_argument('-u', '--user', nargs='*', type=str, required=False, help='User associated with the task', default=["unknown"])

    # Création du parseur pour la commandemodify
    parser_modify = subparsers.add_parser('modify',help='Modify a task given its id. The rest of the command line is used for the task details, the default being "no details"')
    parser_modify.add_argument('id', help="the task id")
    parser_modify.add_argument('new_details',type=str, nargs='*', help="the new details", default=["no details"]) 
    parser_modify.add_argument('-u', '--new_user', nargs='*', required=False, type=str, help='New user associated with the task', default=["None"])
    parser_modify.add_argument('-t', '--est_time', required=False, type=int, help='Set a new estimated time for performing the task', default=None)


    # Création du parseur pour la commanderm
    parser_rm = subparsers.add_parser('rm', help='Remove an task given its id')
    parser_rm.add_argument('id', type=int, help="the task id")

    # Création du parseur pour la commandeshow
    parser_show = subparsers.add_parser('show', help='Show the tasks')

    #Création du parseur pour la commandeend
    parser_end = subparsers.add_parser('end', help='Mark a task as ended')
    parser_end.add_argument('id', type=int, help="The task id")
    parser_end.add_argument('-r','--end_time', required=True, help='Enter the actual time in seconds for performing the task')
    
    #Création du parseur pour la commandecreate
    parser_create = subparsers.add_parser('create', help='Create a new task file')
    parser_create.add_argument('new_file', help='The new tasks file')
    parser_create.add_argument('new_details', type=str, help='The first task')
    parser_creat.add_argument('-u','new_user', type= str, help='The first attributed user')
