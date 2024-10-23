# JeuxOlympiques
Site des Jeux Olympiques

# JOBackOffice

    # Path
    JOBackOffice -> back_end -> (API REST)
    JOBackOffice -> back_office -> (interface admin)

    # Start Project
    python3 manage.py runserve

    # migration DB models
    python3 manage.py makemigrations && python3 manage.py migrate

    # API REST
    End-Point Product (Choix des ticket "Solo", "Duo", "Famille") -> CRUD

    # DataBases
    Postgresql -> Host: 127.0.0.1 -> Port: 5432 -> Name: JeuxOlympiqueDB -> User: postgres -> Password: viny