import skia

surface = skia.Surface(256, 256)

with surface as canvas:
    rect = skia.Rect(50, 50, 90, 110)
    paint = skia.Paint(
        AntiAlias=True,
        Style=skia.Paint.kStroke_Style,
        StrokeWidth=4,
        Color=skia.ColorRED,
    )

    canvas.drawColor(skia.ColorWHITE)
    canvas.drawRect(rect, paint)

    oval = skia.RRect.MakeOval(rect)
    oval.offset(40, 60)
    paint.setColor(skia.ColorBLUE)
    canvas.drawRRect(oval, paint)

    paint.setColor(skia.ColorCYAN)
    canvas.drawCircle(180, 50, 25, paint)

    rect.offset(80, 0)
    paint.setColor(skia.ColorYELLOW)
    canvas.drawRoundRect(rect, 10, 10, paint)

    path = skia.Path()
    path.cubicTo(768, 0, -512, 256, 256, 256)
    paint.setColor(skia.ColorGREEN)
    canvas.drawPath(path, paint)

    paint2 = skia.Paint()
    text = skia.TextBlob('Hello, Skia!', skia.Font(None, 18))
    canvas.drawTextBlob(text, 50, 25, paint2)

image = surface.makeImageSnapshot()
image.save('output.png', skia.kPNG)
