#sample module -- you can see how the magic is done

async def SAMPLE_FUNC(ctx, someArgs):
    await ctx.send(f"From sample module: {str(someArgs)}")


'''
async def new_fun(ctx, yourArgs):
    await ctx.send(f"This is a new function {str(yourArgs)})
'''