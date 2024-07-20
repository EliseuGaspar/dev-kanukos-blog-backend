""""""


#=========================== Estados de uma postagem //
DRAFT = 'draft'
PUBLISHED = 'published'
ARCHIVED = 'archived'

STATUS_CHOICES = [
    (DRAFT, 'Draft'),
    (PUBLISHED, 'Published'),
    (ARCHIVED, 'Archived'),
]

#=========================== Reações de postagens e comentários //
LAUGHTER = '😆'
CONGRATULATIONS = '👏'
ADMIRATION = '😮'
SADNESS = '😢'
ANGER = '😡'

REACTIONS = [
    (LAUGHTER, 'laughter'),
    (CONGRATULATIONS, 'congratulations'),
    (ADMIRATION, 'admiration'),
    (SADNESS, 'sadness'),
    (ANGER, 'anger')
]

#=========================== Categorias de postagens //

DEVELOPMENT = 'development'
NETWORKS = 'networks'
HARDWARE = 'hardware'
DATABASE = 'database'
STREAM = 'stream'
DISCUSSIONS = 'discussions'
MACHINE_LEARNING = 'machine-learning'

CATEGORIES = [
    (DEVELOPMENT, 'development'),
    (NETWORKS, 'networks'),
    (HARDWARE, 'hardware'),
    (DATABASE, 'database'),
    (STREAM, 'stream'),
    (DISCUSSIONS, 'discussions'),
    (MACHINE_LEARNING, 'machine-learning')
]
