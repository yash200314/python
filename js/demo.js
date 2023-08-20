const data = require("./data");

console.log("data",data);
// let array_of_obj= [
//     {
//         "id":1233,
//         "name":"product-1",
//         "price":23,
//         "src":"./some/url"
//     },
//     {
//         "id":1243,
//         "name":"product-2",
//         "price":23,
//         "src":"./some/url"
//     },
//     {
//         "id":1235,
//         "name":"product-3",
//         "price":23,
//         "src":"./some/url"
//     },
//     {
//         "id":233,
//         "name":"product-4",
//         "price":23,
//         "src":"./some/url"
//     },
//     {
//         "id":1233,
//         "name":"product-5",
//         "price":23,
//         "src":"./some/url"
//     },
//     {
//         "id":1239,
//         "name":"product-6",
//         "price":23,
//         "src":"./some/url"
//     }
// ]


// <div display:"flex">
// array_of_obj.map((data,key)=>(
//   <Card marginInline:"20px">
//     <Image src={data.src}></Image>
//     <title>{data.name}</title>
//     <description>{data.desc}</description>
//     <price>{data.price}</price>
//     <cart onClick(()=>dosomething())>buy now</cart>
//   </Card>
// ));
// </div>

data.map((data,key)=>{
console.log(data.id,data.name,data.price)
})