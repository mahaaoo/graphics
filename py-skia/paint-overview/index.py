import skia

surface = skia.Surface(250, 300)

with surface as canvas:
  paint1 = skia.Paint(
    AntiAlias=True,
    Color=skia.Color(255, 0, 0),
    Style=skia.Paint.kFill_Style)

  paint2 = skia.Paint(
      AntiAlias=True,
      Color=skia.Color(0, 136, 0),
      Style=skia.Paint.kStroke_Style,
      StrokeWidth=3)

  paint3 = skia.Paint(
      AntiAlias=True,
      Color=skia.Color(136, 136, 136))

  blob1 = skia.TextBlob("Skia!", skia.Font(None, 64.0, 1.0, 0.0))
  blob2 = skia.TextBlob("Skia!", skia.Font(None, 64.0, 1.5, 0.0))

  canvas.clear(skia.ColorWHITE)
  canvas.drawTextBlob(blob1, 20.0, 64.0, paint1)
  canvas.drawTextBlob(blob1, 20.0, 144.0, paint2)
  canvas.drawTextBlob(blob2, 20.0, 224.0, paint3)


image = surface.makeImageSnapshot()
image.save('output.png', skia.kPNG)
