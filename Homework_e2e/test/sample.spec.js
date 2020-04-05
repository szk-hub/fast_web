describe('render todolist', function () {
  let page;

  before (async function () {
    page = await browser.newPage();
    await page.goto('http://localhost:3000/');
  });

  after (async function () {
    await page.close();
  });

  it('should have correct item', async function() {
    let todoList = await page.waitFor('.todolist');
    const item_le = await page.evaluate(todoList => todoList.children.length, todoList);
    // 上个练习中，将添加条目框跟todolist放在一起了，因此会多出一个长度，不过测试的依旧是总渲染条目数
    expect(item_le).to.eql(3);
  })

});

describe('add todo', function () {
    let page;

    before (async function () {
      page = await browser.newPage();
      await page.goto('http://localhost:3000/');
    });
  
    after (async function () {
      await page.close();
    });

    it('should have correct title', async function() {
        expect(await page.title()).to.eql('React App');
    })   

    it('should new todo correct', async function() {
      await page.type('.same.text', 'new todo item', {delay: 50});
      await page.click('.same.btn', {delay: 500});
      let todoList = await page.waitFor('.todolist');
      const expectInputContent = await page.evaluate(todoList => todoList.lastChild.innerText, todoList);
      expect(expectInputContent).to.eql('new todo item');
    }) 
  });

  describe('modify todo status', function () {
    let page;

    before (async function () {
      page = await browser.newPage();
      await page.goto('http://localhost:3000/');
    });
  
    after (async function () {
      await page.close();
    });

    it('should get correct item status', async function() {
      let item = await page.waitFor('.item');
      const itemContent = await page.evaluate(item => item.innerText, item);
      await page.click('.item', {delay: 500});
      let itemdone = await page.waitFor('.done-item')
      const itemdoneContent = await page.evaluate(itemdone => itemdone.innerText, itemdone);

      expect(itemContent).to.eql(itemdoneContent);
      
    })

  });

  

  