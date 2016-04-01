"""
Collection of mappings for PEP moods/activities
extracted directly from the XEP
"""

MOODS = {
          'afraid': 'Afraid',
          'amazed': 'Amazed',
          'angry': 'Angry',
          'amorous': 'Amorous',
          'annoyed': 'Annoyed',
          'anxious': 'Anxious',
          'aroused': 'Aroused',
          'ashamed': 'Ashamed',
          'bored': 'Bored',
          'brave': 'Brave',
          'calm': 'Calm',
          'cautious': 'Cautious',
          'cold': 'Cold',
          'confident': 'Confident',
          'confused': 'Confused',
          'contemplative': 'Contemplative',
          'contented': 'Contented',
          'cranky': 'Cranky',
          'crazy': 'Crazy',
          'creative': 'Creative',
          'curious': 'Curious',
          'dejected': 'Dejected',
          'depressed': 'Depressed',
          'disappointed': 'Disappointed',
          'disgusted': 'Disgusted',
          'dismayed': 'Dismayed',
          'distracted': 'Distracted',
          'embarrassed': 'Embarrassed',
          'envious': 'Envious',
          'excited': 'Excited',
          'flirtatious': 'Flirtatious',
          'frustrated': 'Frustrated',
          'grumpy': 'Grumpy',
          'guilty': 'Guilty',
          'happy': 'Happy',
          'hopeful': 'Hopeful',
          'hot': 'Hot',
          'humbled': 'Humbled',
          'humiliated': 'Humiliated',
          'hungry': 'Hungry',
          'hurt': 'Hurt',
          'impressed': 'Impressed',
          'in_awe': 'In awe',
          'in_love': 'In love',
          'indignant': 'Indignant',
          'interested': 'Interested',
          'intoxicated': 'Intoxicated',
          'invincible': 'Invincible',
          'jealous': 'Jealous',
          'lonely': 'Lonely',
          'lucky': 'Lucky',
          'mean': 'Mean',
          'moody': 'Moody',
          'nervous': 'Nervous',
          'neutral': 'Neutral',
          'offended': 'Offended',
          'outraged': 'Outraged',
          'playful': 'Playful',
          'proud': 'Proud',
          'relaxed': 'Relaxed',
          'relieved': 'Relieved',
          'remorseful': 'Remorseful',
          'restless': 'Restless',
          'sad': 'Sad',
          'sarcastic': 'Sarcastic',
          'serious': 'Serious',
          'shocked': 'Shocked',
          'shy': 'Shy',
          'sick': 'Sick',
          'sleepy': 'Sleepy',
          'spontaneous': 'Spontaneous',
          'stressed': 'Stressed',
          'strong': 'Strong',
          'surprised': 'Surprised',
          'thankful': 'Thankful',
          'thirsty': 'Thirsty',
          'tired': 'Tired',
          'undefined': 'Undefined',
          'weak': 'Weak',
          'worried': 'Worried'
}




ACTIVITIES = {
        'doing_chores': {
            'category': 'Doing_chores',

            'buying_groceries': 'Buying groceries',
            'cleaning': 'Cleaning',
            'cooking': 'Cooking',
            'doing_maintenance': 'Doing maintenance',
            'doing_the_dishes': 'Doing the dishes',
            'doing_the_laundry': 'Doing the laundry',
            'gardening': 'Gardening',
            'running_an_errand': 'Running an errand',
            'walking_the_dog': 'Walking the dog',
            'other': 'Other',
            },
        'drinking': {
            'category': 'Drinking',

            'having_a_beer': 'Having a beer',
            'having_coffee': 'Having coffee',
            'having_tea': 'Having tea',
            'other': 'Other',
            },
        'eating': {
            'category':'Eating',

            'having_breakfast': 'Having breakfast',
            'having_a_snack': 'Having a snack',
            'having_dinner': 'Having dinner',
            'having_lunch': 'Having lunch',
            'other': 'Other',
            },
        'exercising': {
            'category': 'Exercising',

            'cycling': 'Cycling',
            'dancing': 'Dancing',
            'hiking': 'Hiking',
            'jogging': 'Jogging',
            'playing_sports': 'Playing sports',
            'running': 'Running',
            'skiing': 'Skiing',
            'swimming': 'Swimming',
            'working_out': 'Working out',
            'other': 'Other',
            },
        'grooming': {
            'category': 'Grooming',

            'at_the_spa': 'At the spa',
            'brushing_teeth': 'Brushing teeth',
            'getting_a_haircut': 'Getting a haircut',
            'shaving': 'Shaving',
            'taking_a_bath': 'Taking a bath',
            'taking_a_shower': 'Taking a shower',
            'other': 'Other',
            },
        'having_appointment': {
            'category': 'Having appointment',

            'other': 'Other',
            },
        'inactive': {
            'category': 'Inactive',

            'day_off': 'Day_off',
            'hanging_out': 'Hanging out',
            'hiding': 'Hiding',
            'on_vacation': 'On vacation',
            'praying': 'Praying',
            'scheduled_holiday': 'Scheduled holiday',
            'sleeping': 'Sleeping',
            'thinking': 'Thinking',
            'other': 'Other',
            },
        'relaxing': {
            'category': 'Relaxing',

            'fishing': 'Fishing',
            'gaming': 'Gaming',
            'going_out': 'Going out',
            'partying': 'Partying',
            'reading': 'Reading',
            'rehearsing': 'Rehearsing',
            'shopping': 'Shopping',
            'smoking': 'Smoking',
            'socializing': 'Socializing',
            'sunbathing': 'Sunbathing',
            'watching_a_movie': 'Watching a movie',
            'watching_tv': 'Watching tv',
            'other': 'Other',
            },
        'talking': {
            'category': 'Talking',

            'in_real_life': 'In real life',
            'on_the_phone': 'On the phone',
            'on_video_phone': 'On video phone',
            'other': 'Other',
            },
        'traveling': {
            'category': 'Traveling',

            'commuting': 'Commuting',
            'driving': 'Driving',
            'in_a_car': 'In a car',
            'on_a_bus': 'On a bus',
            'on_a_plane': 'On a plane',
            'on_a_train': 'On a train',
            'on_a_trip': 'On a trip',
            'walking': 'Walking',
            'cycling': 'Cycling',
            'other': 'Other',
            },
        'undefined': {
            'category': 'Undefined',

            'other': 'Other',
            },
        'working': {
            'category': 'Working',

            'coding': 'Coding',
            'in_a_meeting': 'In a meeting',
            'writing': 'Writing',
            'studying': 'Studying',
            'other': 'Other',
            }
        }
