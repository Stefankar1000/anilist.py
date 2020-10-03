from enum import Enum, auto


class UserSort(Enum):
    ID = auto()
    ID_DESC = auto()
    USERNAME = auto()
    USERNAME_DESC = auto()
    WATCHED_TIME = auto()
    WATCHED_TIME_DESC = auto()
    CHAPTERS_READ = auto()
    CHAPTERS_READ_DESC = auto()
    SEARCH_MATCH = auto()


class CharacterSort(Enum):
    ID = auto()
    ID_DESC = auto()
    ROLE = auto()
    ROLE_DESC = auto()
    SEARCH_MATCH = auto()
    FAVOURITES = auto()
    FAVOURITES_DESC = auto()


class MediaSort(Enum):
    ID = auto()
    ID_DESC = auto()
    TITLE_ROMAJI = auto()
    TITLE_ROMAJI_DESC = auto()
    TITLE_ENGLISH = auto()
    TITLE_ENGLISH_DESC = auto()
    TITLE_NATIVE = auto()
    TITLE_NATIVE_DESC = auto()
    TYPE = auto()
    TYPE_DESC = auto()
    FORMAT = auto()
    FORMAT_DESC = auto()
    START_DATE = auto()
    START_DATE_DESC = auto()
    END_DATE = auto()
    END_DATE_DESC = auto()
    SCORE = auto()
    SCORE_DESC = auto()
    POPULARITY = auto()
    POPULARITY_DESC = auto()
    TRENDING = auto()
    TRENDING_DESC = auto()
    EPISODES = auto()
    EPISODES_DESC = auto()
    DURATION = auto()
    DURATION_DESC = auto()
    STATUS = auto()
    STATUS_DESC = auto()
    CHAPTERS = auto()
    CHAPTERS_DESC = auto()
    VOLUMES = auto()
    VOLUMES_DESC = auto()
    UPDATED_AT = auto()
    UPDATED_AT_DESC = auto()
    SEARCH_MATCH = auto()
    FAVOURITES = auto()
    FAVOURITES_DESC = auto()


class StaffSort(Enum):
    ID = auto()
    ID_DESC = auto()
    ROLE = auto()
    ROLE_DESC = auto()
    LANGUAGE = auto()
    LANGUAGE_DESC = auto()
    SEARCH_MATCH = auto()
    FAVOURITES = auto()
    FAVOURITES_DESC = auto()


class StudioSort(Enum):
    ID = auto()
    ID_DESC = auto()
    NAME = auto()
    NAME_DESC = auto()
    SEARCH_MATCH = auto()
    FAVOURITES = auto()
    FAVOURITES_DESC = auto()


class MediaTrendSort(Enum):
    ID = auto()
    ID_DESC = auto()
    MEDIA_ID = auto()
    MEDIA_ID_DESC = auto()
    DATE = auto()
    DATE_DESC = auto()
    SCORE = auto()
    SCORE_DESC = auto()
    POPULARITY = auto()
    POPULARITY_DESC = auto()
    TRENDING = auto()
    TRENDING_DESC = auto()
    EPISODE = auto()
    EPISODE_DESC = auto()


class ReviewSort(Enum):
    ID = auto()
    ID_DESC = auto()
    SCORE = auto()
    SCORE_DESC = auto()
    RATING = auto()
    RATING_DESC = auto()
    CREATED_AT = auto()
    CREATED_AT_DESC = auto()
    UPDATED_AT = auto()
    UPDATED_AT_DESC = auto()


class RecommendationSort(Enum):
    ID = auto()
    ID_DESC = auto()
    RATING = ()
    RATING_DESC = ()


class UserStatisticsSort(Enum):
    ID = auto()
    ID_DESC = auto()
    COUNT = auto()
    COUNT_DESC = auto()
    PROGRESS = auto()
    PROGRESS_DESC = auto()
    MEAN_SCORE = auto()
    MEAN_SCORE_DESC = auto()


class MediaListSort(Enum):
    ID = auto()
    ID_DESC = auto()
    SCORE = auto()
    SCORE_DESC = auto()
    STATUS = auto()
    STATUS_DESC = auto()
    PROGRESS = auto()
    PROGRESS_DESC = auto()
    PROGRESS_VOLUMES = auto()
    PROGRESS_VOLUMES_DESC = auto()
    REPEAT = auto()
    REPEAT_DESC = auto()
    PRIORITY = auto()
    PRIORITY_DESC = auto()
    STARTED_ON = auto()
    STARTED_ON_DESC = auto()
    FINISHED_ON = auto()
    FINISHED_ON_DESC = auto()
    ADDED_TIME = auto()
    ADDED_TIME_DESC = auto()
    UPDATED_TIME = auto()
    UPDATED_TIME_DESC = auto()
    MEDIA_TITLE_ROMAJI = auto()
    MEDIA_TITLE_ROMAJI_DESC = auto()
    MEDIA_TITLE_ENGLISH = auto()
    MEDIA_TITLE_ENGLISH_DESC = auto()
    MEDIA_TITLE_NATIVE = auto()
    MEDIA_TITLE_NATIVE_DESC = auto()
    MEDIA_POPULARITY = auto()
    MEDIA_POPULARITY_DESC = auto()


class AiringSort(Enum):
    ID = auto()
    ID_DESC = auto()
    MEDIA_ID = auto()
    MEDIA_ID_DESC = auto()
    TIME = auto()
    TIME_DESC = auto()
    EPISODE = auto()
    EPISODE_DESC = auto()


class ActivitySort(Enum):
    ID = auto()
    ID_DESC = auto()


class ThreadSort(Enum):
    ID = auto()
    ID_DESC = auto()
    TITLE = auto()
    TITLE_DESC = auto()
    CREATED_AT = auto()
    CREATED_AT_DESC = auto()
    UPDATED_AT = auto()
    UPDATED_AT_DESC = auto()
    REPLIED_AT = auto()
    REPLIED_AT_DESC = auto()
    REPLY_COUNT = auto()
    REPLY_COUNT_DESC = auto()
    VIEW_COUNT = auto()
    VIEW_COUNT_DESC = auto()
    IS_STICKY = auto()
    SEARCH_MATCH = auto()


class ThreadCommentSort(Enum):
    ID = auto()
    ID_DESC = auto()


class SiteTrendSort(Enum):
    DATE = auto()
    DATE_DESC = auto()
    COUNT = auto()
    COUNT_DESC = auto()
    CHANGE = auto()
    CHANGE_DESC = auto()


class SubmissionSort(Enum):
    ID = auto()
    ID_DESC = auto()
