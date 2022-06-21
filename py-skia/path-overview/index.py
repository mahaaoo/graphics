import skia

surface = skia.Surface(200, 200)

with surface as canvas:
  paint = skia.Paint(AntiAlias=True)
  path = skia.Path()
  paint.setColor(skia.ColorRED)
  path.moveTo(124, 108)
  path.lineTo(172, 24)
  path.addCircle(50, 50, 30)
  path.moveTo(36, 148)
  path.quadTo(66, 188, 120, 136)
  canvas.drawPath(path, paint)

  paint.setStyle(skia.Paint.kStroke_Style);
  paint.setColor(skia.ColorBLUE)
  paint.setStrokeWidth(3)
  canvas.drawPath(path, paint)

image = surface.makeImageSnapshot()
image.save('output.png', skia.kPNG)
