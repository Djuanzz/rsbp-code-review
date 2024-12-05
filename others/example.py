import openai

openai.api_key = 'pk-zTZsQRMeMVNLUdJViRQEFZtkjToFrxeFlyFoINazLUdNOkKi'
openai.api_base = "https://api.pawan.krd/pai-001/v1"

code = """func (uc *userController) Register(ctx *gin.Context) {
	var userReq dto.UserRegisterReq

	if err := ctx.ShouldBind(&userReq); err != nil {
		res := utils.ResponseFailed(dto.MSG_USER_REGISTER_FAILED, err.Error())
		ctx.AbortWithStatusJSON(http.StatusBadRequest, res)
		return
	}

	response, err := uc.userService.Register(userReq)

	if err != nil {
		res := utils.ResponseFailed(dto.MSG_USER_REGISTER_FAILED, err.Error())
		ctx.AbortWithStatusJSON(http.StatusInternalServerError, res)
		return
	}

	res := utils.ResponseSuccess(dto.MSG_USER_REGISTER_SUCCESS, response)
	ctx.JSON(http.StatusCreated, res)
}
"""

res = openai.ChatCompletion.create(
    model="pai-001",
    messages=[
        {"role": "system", "content": f"""
		Please review the code below and identify any syntax or logical errors, suggest
		ways to refactor and improve code quality, enhance performance, address security
		concerns, and align with best practices. Provide specific examples for each area
		and limit your recommendations to three per category.

		Use the following response format, keeping the section headings as-is, and provide
		your feedback. Use bullet points for each response. The provided examples are for
		illustration purposes only and should not be repeated.

		**Syntax and logical errors (example)**:
		- Incorrect indentation on line 12
		- Missing closing parenthesis on line 23

		Code:
		```
		{code}
		```

		Your review: """}
    ]
)

print(res.choices[0].message['content'])