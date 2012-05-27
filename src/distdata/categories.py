import distdata.connection
import distdata.questions

def getData():
    data = {}
    categories = __getCategoriesCollection()
    for category in categories.find():
        data[category["_id"]] = category["num_questions"]
    return data

def _updateCategoryData():
    tags = {}
    for question in distdata.questions.__getQuestionsCollection().find():
        for tag in question["tags"]:
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1
    categories = __getCategoriesCollectionNoUpdate()
    for tag in tags.keys():
        category_data = categories.find_one({"_id":tag})
        if not category_data:
            category_data = {"_id":tag}
        category_data["num_questions"] = tags[tag]
        categories.save(category_data)

def __getCategoriesCollectionNoUpdate():
    return distdata.connection.getTechquizDb().categories

def __getCategoriesCollection():
    categories = __getCategoriesCollectionNoUpdate()
    if categories.count() is 0:
        _updateCategoryData()
    return categories 

if __name__ == '__main__':
#    categories = __getCategoriesCollection()
#    for category in categories.find():
#        print category
    print getData()
    
