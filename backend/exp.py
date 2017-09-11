class Student(Resource):
    def get(self, registration=None, department=None):
        data = []

        if registration:
            studnet_info = mongo.db.student.find_one({"registration": registration}, {"_id": 0})
            if studnet_info:
                return jsonify({"status": "ok", "data": studnet_info})
            else:
                return {"response": "no student found for {}".format(registration)}

        elif department:
            cursor = mongo.db.student.find({"department": department}, {"_id": 0}).limit(10)
            for student in cursor:
                student['url'] = APP_URL + url_for('students') + "/" + student.get('registration')
                data.append(student)

            return jsonify({"department": department, "response": data})
else:
            cursor = mongo.db.student.find({}, {"_id": 0, "update_time": 0}).limit(10)

            for student in cursor:
                print student
                student['url'] = APP_URL + url_for('students') + "/" + student.get('registration')
                data.append(student)

            return jsonify({"response": data})

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            registration = data.get('registration')
            if registration:
                if mongo.db.student.find_one({"registration": registration}):
                    return {"response": "student already exists."}
                else:
                    mongo.db.student.insert(data)
            else:
                return {"response": "registration number missing"}

        return redirect(url_for("students"))

