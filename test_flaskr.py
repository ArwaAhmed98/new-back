import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://postgresql:123@localhost:5432/trivia"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            #give the attribuites of the class any values
        self.new_Q={ 
            'question' : 'How are you ? ',
            'answer' : 'Fine,Thanks',
          'difficulty': 1,
            'category': '1'}
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # def test_get_paginated_questions(self):
    #     res=self.client().get('/questions')
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code,200)
    #     self.assertEqual(data['success'],True)
    #     self.assertTrue(data['total_questions'])
        
    # def test_404_sent_requesting_beyond_valid_page(self):
        
    #     res=self.client().get('/questions?page=1000') 
    #     #Check that 404 not found will pop up for a fake data 
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code,404)
    #     self.assertEqual(data['success', False])
    #     self.assertEqual(['message'] , 'resource Not found')
    # def test_add_question(self):
        
    #     new_question = {
    #     'question': 'new question',
    #     'answer': 'new answer',
    #     'difficulty': 1,
    #     'category': 1}
    #     total_questions_before = len(Question.query.all())
    #     res = self.client().post('/questions', json=new_question)
    #     data = json.loads(res.data)
    #     total_questions_after = len(Question.query.all())

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(total_questions_after, total_questions_before + 1)

    # def test_422_add_question(self):
    #     new_question = {
    #         'question': 'new_question',
    #         'answer': 'new_answer',
    #         'category': 1
    #     }
    #     res = self.client().post('/questions', json=new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "unprocessable")
    # print("helllooooooooooooooo")
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()