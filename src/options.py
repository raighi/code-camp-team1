import argparse


def create_parser():

    # Création du parseur de ligne de commande
    parser = argparse.ArgumentParser(prog='Task_manager', 
                                     description='A simple task manager')
    # Ajout d’un argumentpositionnel (le fichier contenant les tâches)
    parser.add_argument('file', help='The tasks file')

    # Ajout d’un sous-parseur pour les sous-commandes
    subparsers = parser.add_subparsers(help='The commands to manage orders',
                                       dest='command', required=True)

    # Création du parseur pour la commandeadd
    parser_add = subparsers.add_parser('add', help='Add a new task. '
                                       'The rest of the command line is used for the task details, '
                                       'the default being "no details".')
    parser_add.add_argument('details', nargs='*', default=["no details"],
                            help="task details")
    parser_add.add_argument('-u', '--user', nargs='*', type=str, required=False, help='User associated with the task',
                            default=["unknown"])
    # Création du parseur pour la commandemodify
    parser_modify = subparsers.add_parser('modify', help='Modify a task given its id. The rest of the command line is '
                                          'used for the task details, the default being "no details"')
    parser_modify.add_argument('id', help="the task id")
    parser_modify.add_argument('new_details', type=str, nargs='*', help="the new details", default=["no details"])
    parser_modify.add_argument('-u', '--new_user', nargs='*', required=False, type=str,
                               help='New user associated with the task', default=["None"])
    parser_modify.add_argument('-t', '--est_time', required=False, type=int,
                               help='Set a new estimated time for performing the task', default=None)
    # Création du parseur pour la commanderm
    parser_rm = subparsers.add_parser('rm', help='Remove an task given its id')
    parser_rm.add_argument('id', type=int, help="the task id")
    # Création du parseur pour la commandeshow
    _ = subparsers.add_parser('show', help='Show the tasks')
    # Création du parseur pour la commande end
    parser_end = subparsers.add_parser('end', help='Mark a task as ended')
    parser_end.add_argument('id', help="The task id")
    parser_end.add_argument('-r', '--end_time', required=True,
                            help='Enter the actual time in seconds for performing the task')
    return parser
