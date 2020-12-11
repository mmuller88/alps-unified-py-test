import alps_unified_ts as alps

# alps = alps_unified_ts.Alps.unified(alps_document=alps_unified_ts.Alps.load_yaml("todo-alps.yaml"), format_type=alps_unified_ts.FormatType.OPENAPI)
# print(alps)

alps_def = alps.AlpsDef(
    version='1.0', 
    descriptor=[alps.DescriptorDef(id="id", type="semantic", text="sotrage id of todo item")], 
    doc=alps.DocDef(
        value="Simple Todo list example"), 
        ext=[
            alps.ExtDef(
                name="root", 
                tags="oas", 
                type="metadata", 
                value="http://api.example.org/todo"),
            alps.ExtDef(
                name="title", 
                tags="oas", 
                type="metadata", 
                value="simpleTodo")])

alps_converted = alps.Alps.unified(alps_document=alps.Alps.spec(alps=alps_def), format_type=alps.FormatType.OPENAPI)
print(alps_converted)