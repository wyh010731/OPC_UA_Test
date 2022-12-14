const web_url = "http://127.0.0.1:8987/";

function OPC_Read(node)
{
  $.ajax({
    url: web_url+"index",
    type: "POST",
    data: {"person":node},
    dataType: "json",
    success:function (result){
      $("#dis"+node).text(result.person);
    }
  })
}

function OPC_Write(node,value)
{
   $.ajax({
    url:web_url+"index1",
    type:"POST",
    data:{"node":node,"value":value},
    success:function (result1){
      if(result1=="ok")
      {
          alert("写入成功！")
      }
    }
  }
  )}
