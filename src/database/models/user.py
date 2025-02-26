from mongoengine import Document, StringField, EmailField, DateTimeField, EnumField
from enum import Enum
from datetime import datetime
import bcrypt

class UserRole(Enum):
    ADMIN = 'admin'
    MANAGER = 'manager'
    EMPLOYEE = 'employee'

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password_hash = StringField(required=True)
    role = EnumField(UserRole, required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    last_login = DateTimeField()
    
    meta = {
        'collection': 'users',
        'indexes': [
            'username',
            'email',
            'role'
        ]
    }
    
    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    @classmethod
    def authenticate(cls, username, password):
        user = cls.objects(username=username).first()
        if user and user.verify_password(password):
            user.last_login = datetime.utcnow()
            user.save()
            return user
        return None
    
    def has_permission(self, permission):
        """Check if user has specific permission based on role"""
        role_permissions = {
            UserRole.ADMIN: ['manage_users', 'process_payroll', 'view_reports', 'manage_system'],
            UserRole.MANAGER: ['view_team_payroll', 'approve_attendance', 'manage_performance'],
            UserRole.EMPLOYEE: ['view_personal_info', 'track_attendance', 'manage_benefits']
        }
        return permission in role_permissions.get(self.role, [])