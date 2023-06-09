第十二章分布式系统安全

1. 请解释分布式系统当中的日蚀攻击和拜占庭节点攻击

分布式系统的两种常见攻击方式是日蚀攻击（Eclipse Attack）和拜占庭节点攻击（Byzantine Fault）。

1. 日蚀攻击：在日蚀攻击中，攻击者试图完全控制或影响目标节点在网络中的视图，使其只能看到攻击者控制的节点，从而阻断目标节点和诚实节点的联系。这样，攻击者就可以通过在目标节点看到的所有信息中进行篡改或伪造，对目标节点进行欺骗，达到攻击者的目的。

例如，在比特币网络中，如果攻击者可以控制一个节点所连接的所有其他节点（也就是说，攻击者“遮蔽”了这个节点的网络视图），那么这个节点就可能被欺骗，认为一个无效的交易是有效的，或者被错误地告知网络已经在某个无效的区块上达成共识。

2. 拜占庭节点攻击：拜占庭节点攻击源自著名的拜占庭将军问题，这是一个关于网络可靠性的经典问题。在这个问题中，若有一个或多个节点（将军）表现出故障或恶意行为（比如发送错误信息或者发送混乱的消息），那么网络如何保证其余的节点能够达成一致就成为了一个挑战。如果一个系统能够容忍拜占庭故障，那么就意味着这个系统可以即使在存在恶意节点或故障节点的情况下，仍能保持正常运行。

例如，在区块链网络中，如果有一部分节点试图通过发布虚假的交易或区块来欺骗网络，那么网络必须有能力忽视这些欺骗性的信息，并在其余诚实节点之间达成一致。

这两种攻击都是分布式系统需要解决的安全问题。为了抵抗这些攻击，研究人员已经提出了很多策略，包括设计更为复杂的共识算法，以及采取特殊的网络拓扑结构等等。

第十三章应用安全

1. 请解释XSS攻击的原理，简述一种防御方法并简单分析原因
跨站脚本攻击（Cross-Site Scripting，简称 XSS）是一种常见的网络安全攻击手段。其基本原理是攻击者向网站注入恶意的脚本，当其他用户浏览到这个网页时，这些恶意脚本就会执行，从而达到攻击目的。这些攻击可能包括盗取用户的登录凭证、操纵网站的内容等。

以下是一个简单的例子：攻击者可能会在评论或者论坛中，留下一段看起来像正常评论的代码，比如`<img src="x" onerror="stealYourCookies()">`。当其他用户浏览到这个评论时，`stealYourCookies`函数就会在他们的浏览器中执行，可能盗取他们的cookies。

防御XSS攻击的一种有效方法是使用输入过滤（Input Sanitization）。简单来说，就是检查用户提交的数据是否包含可能引发XSS攻击的内容，如果包含，就不允许提交或者对其进行转义处理。

例如，如果一个网站允许用户提交包含HTML标签的内容，那么就应该过滤掉一些可能引发XSS攻击的属性，如"onerror"，"onload"等。同时，不应该允许用户提交像`<script>`这样的标签。另外，对于用户提交的URL，应该确保其只能包含http或https这样的安全协议，而不能包含javascript:等可能引发XSS的协议。

这种方法能有效防止XSS的原因在于，XSS攻击的成功要依赖于在用户浏览器中执行恶意脚本，而这些脚本通常会隐藏在用户提交的数据中。通过过滤或转义用户的输入，我们可以阻止这些恶意脚本被插入到网页中，从而防止XSS攻击。








2. 请解释SQL注入攻击的基本原理和防御的基本原理

SQL注入攻击是一种常见的网络攻击手段。其基本原理是攻击者在应用程序的输入字段中输入一段SQL代码，使得这段代码被拼接到应用程序原本要执行的SQL查询语句中，从而改变原本查询语句的语义，实现攻击目的。这些攻击可能包括获取、修改或删除数据库中的敏感信息，或者执行其他恶意操作。

例如，一个简单的登录系统可能会使用类似于以下的查询来验证用户的用户名和密码：`SELECT * FROM users WHERE username = '[username]' AND password = '[password]'`。如果攻击者在用户名字段中输入 `' OR '1'='1`，那么查询语句就会变成 `SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '[password]'`。这个查询的结果总是为真，攻击者就能在不知道密码的情况下登录系统。

防御SQL注入攻击的一个基本原理是预编译SQL查询和参数化查询（Prepared Statements and Parameterized Queries）。预编译和参数化查询能有效防止SQL注入，因为它们明确地区分了查询语句和查询参数。当查询被预编译后，即使参数包含了SQL语句，数据库也不会将这部分内容作为查询语句来执行。

例如，使用参数化查询，上面的查询语句就会变成类似于下面的样子：`SELECT * FROM users WHERE username = ? AND password = ?`。这个查询语句中，`?`是参数的占位符，实际的参数值会在后续单独传递给数据库。这样，即使攻击者在输入字段中输入SQL语句，也只会被当作普通的字符串处理，而不会被执行。

另一种防御方法是对用户的输入进行严格的验证和过滤，避免输入包含可能引发SQL注入的内容。例如，可以限制用户名只能包含字母和数字，而不能包含特殊字符或SQL关键字。

最后，最小权限原则（Principle of Least Privilege）也是一种重要的防御手段。也就是说，应用程序连接数据库的账户只应具有执行其功能所需的最小权限，不应该有修改表结构或删除表的权限。这样，即使遭到SQL注入攻击，攻击者也无法通过这个账户进行破坏性操作。







第十四章人工智能安全





1. 请解释人工智能算法的鲁棒性和可解释性


在人工智能（AI）中，鲁棒性和可解释性是两个非常重要的概念。

1. 鲁棒性：鲁棒性指的是AI系统在面对输入的微小变化或者异常值时，输出的稳定性和准确性。具备鲁棒性的模型能够抵抗诸如噪声、扰动、异常数据、缺失值等的干扰，依然能够给出正确且稳定的输出。对于AI来说，尤其是对于深度学习模型，鲁棒性是一项重要的挑战。例如，在对抗性攻击中，攻击者会故意对输入数据添加微小的、人眼难以察觉的扰动，使得深度学习模型的输出发生大的变化，从而突破模型的安全防护。

2. 可解释性：可解释性指的是AI模型的决策过程能够被人理解和解释的程度。一个具有可解释性的模型，用户可以理解其输出结果是怎么来的，以及在特定输入下模型做出某种决策的原因。对于许多应用，如医疗诊断、金融决策等，可解释性是非常重要的。然而，尤其是对于深度学习模型，由于其复杂的非线性结构和高度的参数化，理解模型内部的决策过程通常是非常困难的，使得深度学习模型被许多人视为“黑箱”。

在AI研究中，鲁棒性和可解释性是两个重要且相互关联的问题。提高模型的鲁棒性可以提高模型在面对各种干扰和攻击时的性能和安全性。提高模型的可解释性可以帮助人们理解和信任模型的决策，也有助于找出模型的不足，从而提高模型的性能。因此，这两个问题都是当前AI研究的重要方向。





2. 请简述投毒攻击和对抗攻击的不同点，请利用“自动驾驶”为场景各举一例


投毒攻击（Poisoning Attack）和对抗攻击（Adversarial Attack）都是针对机器学习模型的攻击方式，但他们的攻击方式和目标有所不同。

1. 投毒攻击是在模型训练阶段进行的。攻击者会添加一些恶意的训练样本到训练集中，使得模型在训练过程中学到错误的模式，从而影响模型在后续的预测。例如，在自动驾驶的场景中，攻击者可能会向训练集中添加一些错误标注的交通标志的图片（例如将停止标志标注为速度限制标志），使得模型在训练过程中学到错误的模式，以后在看到停止标志时可能会错误地识别为速度限制标志。

2. 对抗攻击则是在模型部署后进行的。攻击者会对模型的输入添加微小的、人眼难以察觉的扰动，使得模型的输出发生大的变化。例如，在自动驾驶的场景中，攻击者可能会在停止标志上添加微小的、人眼难以察觉的贴纸或涂鸦，使得自动驾驶系统看到这个停止标志时会错误地识别为其他标志，如速度限制标志。

总的来说，投毒攻击主要是通过篡改训练数据来影响模型的训练，而对抗攻击则是通过在测试阶段篡改输入来误导模型的预测。对于防御这两种攻击，可能需要使用不同的方法和技术。对于投毒攻击，可能需要使用更加严格的数据清洗和验证技术来保证训练数据的质量。对于对抗攻击，可能需要使用对抗训练、模型鲁棒性增强或输入的滤波等技术来提高模型的鲁棒性。







