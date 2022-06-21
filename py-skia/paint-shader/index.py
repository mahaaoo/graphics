import skia

surface = skia.Surface(256, 256)

with surface as canvas:
  paint = skia.Paint(
      Shader=skia.GradientShader.MakeLinear(
          points=[(0.0, 0.0), (256.0, 256.0)],
          colors=[0xFF0000FF, 0xFFFFFF00]))
  canvas.drawPaint(paint)


image = surface.makeImageSnapshot()
image.save('output.png', skia.kPNG)
