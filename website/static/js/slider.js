
(function ($) {
  // Variables
  const $rangeSlider = $('#range-sliders .range-slider');
  const $inputSlider = $('#range-sliders .input-slider');

  // Bg Init
  const bgInit = ($this, val = 0, min = 0, max = 255, color = '#75A1FF') => {
    // Background Change
    const valBg = (val - min) / (max - min) * 100;
    $this.css('background', `linear-gradient(to right, ${color} 0%, ${color} ${valBg}%, #393939 ${valBg}%, #393939 100%)`);
  };

  // Pre Init
  const preInit = () => {
    const rangeSliders = ['range-slider', 'range-slider-1', 'range-slider-2', 'range-slider-3', 'range-slider-4'];
    rangeSliders.forEach(function (key) {
      // Background Change
      const $this = $(`#${key}`);
      const val = Number($this.val());
      const min = Number($this.attr('min'));
      const max = Number($this.attr('max'));
      const color = $this.data('color');
      bgInit($this, val, min, max, color);
    });
  };

  // Toggle Class
  const init = () => {
    // Slider Range Change or Input
    $rangeSlider.off('change input').on('change input', function (e) {
      // Prevent Default
      e.preventDefault();
      e.stopPropagation();

      // Background Change
      const $this = $(this);
      const val = Number($this.val());
      const min = Number($this.attr('min'));
      const max = Number($this.attr('max'));
      const color = $this.data('color');
      bgInit($this, val, min, max, color);

      // Assign value to slider input
      $this.next().val($(this).val());
    });

    // Input Slider Input
    $inputSlider.off('input').on('input', function (e) {
      // Prevent Default
      e.preventDefault();
      e.stopPropagation();


      // Assign value to slider range.
      $this.val(val);
    });
  };

  // Document Ready
  $(function () {
    preInit();
    init();
  });
})(jQuery);

// $('.bmi-form input').on('keypress', function(e) {
//   return e.which !== 13;
// });
