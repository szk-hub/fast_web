const {
    app
  } = require('../src/app');

const{
    asyncReadFile,
    asyncWriteFile
} = require('../src/dao')

const request = require('supertest');

describe("app", () => {
    describe("get request", () => {
      it("should get todo list when request url pattern is '/todo'", (done) => {
        app.locals.dataFilePath = "./test/fixture.json"
        request(app).get('/todo').expect(200).expect([{
            "id": 1,
            "content": "Restful API homework",
            "createdTime": "2019-05-15T00:00:00Z"     
        },
        {
            "id":2,
            "content":"MVC homework",
            "createdTime":"2020-01-01T00:00:00Z"
      }
        ]).end((err, res) => {
          if (err) throw err;
          done()
        })
      })
  
      it("should get specific todo when request url patten is '/todo/:id'", (done) => {
        request(app).get('/todo/1').expect(200).expect({
            "id": 1,
            "content": "Restful API homework",
            "createdTime": "2019-05-15T00:00:00Z"
        }).end((err, res) => {
          if (err) throw err;
          done()
        })
      })
    })
  
    
  })