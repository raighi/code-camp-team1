# !/usr/bin/env python3
import commands
# import core
from options import create_parser


def main():
    options = create_parser().parse_args()  # Récupération des options de la ligne de commande
    try:
        # tasks = core.read_tasks(options.file)
        if options.command == 'add':   # Cas de la commande add
            # Appel de la fonction add et attibution des paramètres récupérés par le parser
            commands.add(details=' '.join(options.details), user=' '.join(options.user), file=options.file)
        if options.command == 'create':   # Cas de la commande create
            # Appel de la fonction create et attibution des paramètres récupérés par le parser
            commands.create(new_file=options.file, new_details=' '.join([options.new_details]),
                            new_user=' '.join(options.new_user))
        elif options.command == 'modify':  # Cas de la commande modify
            # Appel de la fonction modify et attibution des paramètres récupérés par le parser,
            # avec un cas pour résoudre des erreurs liées à l'argument optionnel user (Auteur Thomas)
            commands.modify(id=options.id, new_details=' '.join(options.details),
                            new_user=' '.join(options.user) if options.user is not None else "unknown",
                            file=options.file)
        elif options.command == 'rm':  # Cas de la commande rm
            # Appel de la fonction rm et attibution des paramètres récupérés par le parser
            commands.rm(id=options.id, file=options.file)
        elif options.command == 'show':   # Cas de la commande show
            # Appel de la fonction show et attibution des paramètres récupérés par le parser
            commands.show(file=options.file)
        elif options.command == 'end':   # Cas de la commande end
            #  Appel de la fonction endTask et attibution des paramètres récupérés par le parser (Auteur Raphaël)
            commands.endTask(file=options.file, id=options.id, end_time=' '.join(options.realisedTime))
    except Exception as e:   # Gestion des erreurs
        print(f"An error occurred: {e}")   # Affichage de l'erreur


if __name__ == '__main__':
    main()
