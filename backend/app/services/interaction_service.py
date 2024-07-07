# app/services/interaction_service.py
from app.dal.interaction_repository import InteractionRepository
from datetime import datetime

class InteractionService:
    @staticmethod
    def record_interaction(user_id, book_id, interaction_type, duration=None):
        InteractionRepository.add_interaction(user_id, book_id, interaction_type, datetime.now(), duration)
        
    @staticmethod
    def get_all_interactions():
        return InteractionRepository.dal_get_all_interactions()
        
    @staticmethod
    def get_user_interactions(user_id):
        return InteractionRepository.dal_get_user_interactions(user_id)
